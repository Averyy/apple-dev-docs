# Audio Components

**Framework**: Audio Toolbox

Find, load, and configure audio components, such as Audio Units and audio codecs.

#### Overview

Use the Audio Components API to register and discover audio units, codecs, and other loadable code modules. This API replaces the Component Manager API used prior to macOS 10.6. The system searches for loadable bundles with a `.audiocomp` or `.component` filename extension in the following locations:

- `~/Library/Audio/Plug-Ins/Components`
- `/Library/Audio/Plug-Ins/Components`
- `/System/Library/Components`

The bundle `Info.plist` file needs to contain an `AudioComponents` item whose value is an array of dictionaries. For example:

```swift
<key>AudioComponents</key>
<array>
    <dict>
        <key>type</key>
        <string>aufx</string>
        <key>subtype</key>
        <string>XMPL</string>
        <key>manufacturer</key>
        <string>ACME</string>
        <key>name</key>
        <string>AUExample</string>
        <key>version</key>
        <integer>12345</integer>
        <key>factoryFunction</key>
        <string>AUExampleFactory</string>
        
        <!-- An AudioComponent is sandbox safe. -->
        
        <key>sandboxSafe</key>
        <true/>
        
        <!-- Or it can describe its resource usage. -->
        
        <key>resourceUsage</key>
        <dict>
            <key>iokit.user-client</key>
            <array>
                <string>CustomUserClient1</string>
                <string>CustomUserClient2</string>
            </array>
            <key>mach-lookup.global-name</key>
            <array>
                <string>MachServiceName1</string>
                <string>MachServiceName2</string>
            </array>
            <key>network.client</key>
            <true/>
            <key>temporary-exception.files.all.read-write</key>
            </true>
        </dict>

        <!-- An AudioComponent can define its tags. -->
        
        <key>tags</key>
        <array>
            <string>Effect</string>
            <string>Equalizer</string>
        </array>
    </dict>
</array>
```

## Topics

### Creating an Audio Component Instance
- [func AudioComponentInstanceNew(AudioComponent, UnsafeMutablePointer<AudioComponentInstance?>) -> OSStatus](audiocomponentinstancenew(_:_:).md)
  Creates a new instance of an audio component.
- [func AudioComponentInstantiate(AudioComponent, AudioComponentInstantiationOptions, (AudioComponentInstance?, OSStatus) -> Void)](audiocomponentinstantiate(_:_:_:).md)
- [func AudioComponentInstanceDispose(AudioComponentInstance) -> OSStatus](audiocomponentinstancedispose(_:).md)
  Disposes of an audio component instance.
- [typealias AudioComponent](audiocomponent.md)
  An audio component.
- [struct AudioComponentInstantiationOptions](audiocomponentinstantiationoptions.md)
- [Audio Component Errors](1619490-audio-component-errors.md)
### Creating an Audio Component Dynamically
- [func AudioComponentRegister(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioComponentFactoryFunction) -> AudioComponent](audiocomponentregister(_:_:_:_:).md)
- [func AudioComponentCount(UnsafePointer<AudioComponentDescription>) -> UInt32](audiocomponentcount(_:).md)
  Returns the number of audio components that match a specified `AudioComponentDescription` structure.
- [func AudioComponentFindNext(AudioComponent?, UnsafePointer<AudioComponentDescription>) -> AudioComponent?](audiocomponentfindnext(_:_:).md)
  Finds the next component that matches a specified `AudioComponentDescription` structure after a specified audio component.
- [func AudioComponentInstanceGetComponent(AudioComponentInstance) -> AudioComponent](audiocomponentinstancegetcomponent(_:).md)
  Retrieves a reference to an audio component from an instance of that audio component.
- [struct AudioComponentDescription](audiocomponentdescription.md)
  Identifying information for an audio component.
- [typealias AudioComponentInstance](audiocomponentinstance.md)
  A component instance, or object, is an audio unit or audio codec.
- [struct AudioComponentFlags](audiocomponentflags.md)
- [typealias AudioComponentFactoryFunction](audiocomponentfactoryfunction.md)
### Getting Information About a Component
- [func AudioComponentInstanceCanDo(AudioComponentInstance, Int16) -> Bool](audiocomponentinstancecando(_:_:).md)
  Determines if an audio component instance implements a particular function.
- [func AudioComponentGetDescription(AudioComponent, UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus](audiocomponentgetdescription(_:_:).md)
  Gets the class description, as an `AudioComponentDescription` structure, of an audio component.
- [func AudioComponentCopyName(AudioComponent, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](audiocomponentcopyname(_:_:).md)
  Returns the generic name of an audio component.
- [func AudioComponentGetVersion(AudioComponent, UnsafeMutablePointer<UInt32>) -> OSStatus](audiocomponentgetversion(_:_:).md)
  Gets the version of an audio component in hexadecimal form as `0xMMMMmmDD` (major, minor, dot).
- [func AudioComponentCopyIcon(AudioComponent) -> UIImage?](audiocomponentcopyicon(_:).md)
- [func AudioComponentCopyConfigurationInfo(AudioComponent, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](audiocomponentcopyconfigurationinfo(_:_:).md)
- [struct AudioComponentPlugInInterface](audiocomponentplugininterface.md)
- [typealias AudioComponentMethod](audiocomponentmethod.md)
### Validating an Audio Component
- [func AudioComponentValidate(AudioComponent, CFDictionary?, UnsafeMutablePointer<AudioComponentValidationResult>) -> OSStatus](audiocomponentvalidate(_:_:_:).md)
- [var kAudioComponentValidationParameter_LoadOutOfProcess: String](kaudiocomponentvalidationparameter_loadoutofprocess.md)
- [enum AudioComponentValidationResult](audiocomponentvalidationresult.md)
### Constants
- [var kAudioComponentConfigurationInfo_ValidationResult: String](kaudiocomponentconfigurationinfo_validationresult.md)
- [let kAudioComponentInstanceInvalidationNotification: CFString](kaudiocomponentinstanceinvalidationnotification.md)
- [let kAudioComponentRegistrationsChangedNotification: CFString](kaudiocomponentregistrationschangednotification.md)
- [var kAudioComponentValidationParameter_ForceValidation: String](kaudiocomponentvalidationparameter_forcevalidation.md)
- [var kAudioComponentValidationParameter_TimeOut: String](kaudiocomponentvalidationparameter_timeout.md)

## See Also

- [Generating spatial audio from a multichannel audio stream](generating-spatial-audio-from-a-multichannel-audio-stream.md)
  Convert 8-channel audio to 2-channel spatial audio by using a spatial mixer audio unit.
- [Audio Unit v3 Plug-Ins](audio-unit-v3-plug-ins.md)
  Deliver custom audio effects, instruments, and other audio behaviors using an Audio Unit v3 app extension.
- [Audio Unit v2 (C) API](audio-unit-v2-c-api.md)
  Configure an Audio Unit and prepare it to render audio.
- [Audio Unit Properties](audio-unit-properties.md)
  Obtain information about the built-in mixers, equalizers, filters, effects, and other Audio Unit app extensions.
- [Audio Unit Voice I/O](audio-unit-voice-i-o.md)
  Configure system voice processing and respond to speech events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-components)*