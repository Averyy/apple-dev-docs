# disableLanguageOptionCommand

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The command object for disabling a language option

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var disableLanguageOptionCommand: MPRemoteCommand { get }
```

```objc
@property (nonatomic, readonly) MPRemoteCommand * disableLanguageOptionCommand;
```

#### Discussion

Use the object in this property to register your app’s handler for disabling the language option for the media item. In your handler, change the language option to the new value. You can disable the command if your app does not support it.

## See Also

### Enabling language options
- [var enableLanguageOptionCommand: MPRemoteCommand](./enablelanguageoptioncommand.md)
  The command object for enabling a language option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/disablelanguageoptioncommand)*