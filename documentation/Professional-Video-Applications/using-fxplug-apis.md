# Using FxPlug APIs

**Framework**: Professional-Video-Applications  
**Role**: Article

Use various FxPlug APIs to communicate with host apps like Motion or Final Cut Pro.

#### Overview

When your plug-in needs to access a host’s capabilities, use the associated FxPlug API that corresponds to the capability you need to access.

Your plug-in can instantiate host API objects that let you communicate and interact with the host application to extend your plug-in’s functionality. A host API implements methods that your plug-in can call to get a specific functionality—such as requesting information about a video stream, or reading a parameter value from the UI.

A host API is analogous to a callback suite in other plug-in architectures, but is implemented as a protocol in FxPlug.

FxPlug defines host protocols for common tasks, including:

- Requesting layer information
- Converting between canvas and object coordinate spaces
- Building a list of plug-in parameters
- Getting and setting parameter values
- Evaluating input images at arbitrary times

> **Note**:  Not all host applications support all of the host API protocols in FxPlug. Make sure your plug-in requests the host API object before invoking its methods.

##### Get the most recent versions for host APIs

In FxPlug, you may see similar APIs, differing by only a version number appended at the end. You should always use the latest version available for your plug-in. FxPlug 4 only supports the latest versions. FxPlug includes older versions of the host APIs so previous plug-ins continue to work, unless otherwise marked as deprecated. However, improved and expanded functionality is only available in the latest versions. For example, choose [`FxParameterCreationAPI_v5`](../professional_video_applications/fxparametercreationapi_v5.md), as earlier versions aren’t accessible in FxPlug 4.

##### Use a host API

In this example, you find a slider’s value at a particular render time. In the [`pluginState(_:at:quality:)`](../professional_video_applications/fxtileableeffect/pluginstate%28_,at,quality%29.md) method, you use the latest version of the parameter retrieval host API ([`FxParameterRetrievalAPI_v6`](../professional_video_applications/fxparameterretrievalapi_v6.md)) to retrieve a brightness value created in your plug-in’s [`addParameters()`](../professional_video_applications/fxtileableeffect/addparameters%28%29.md) method. Then add the value to pluginState NSData object for later retrieval.

**Swift**:

```swift
func pluginState(_ pluginState: AutoreleasingUnsafeMutablePointer<NSData>?, at renderTime: CMTime, quality qualityLevel: UInt) throws {
        let paramAPI = _apiManager!.api(for: FxParameterRetrievalAPI_v6.self) as! FxParameterRetrievalAPI_v6
        
        var brightness = 1.0
        paramAPI.getFloatValue(UnsafeMutablePointer<Double>(&brightness), fromParameter: 1, at: renderTime)
        
        pluginState?.pointee = NSData.init(bytes: &brightness, length: MemoryLayout.size(ofValue: brightness))
    }
```

**Objective-C**:

```objc
- (BOOL)pluginState:(NSData * _Nonnull *)pluginState
             atTime:(CMTime)renderTime
            quality:(FxQuality)qualityLevel
              error:(NSError * _Nullable *)error
{
    BOOL    succeeded = NO;
    id<FxParameterRetrievalAPI_v6>  paramGetAPI = [_apiManager apiForProtocol:@protocol(FxParameterRetrievalAPI_v6)];
    if (paramGetAPI != nil)
    {
        double  brightness  = 1.0;
        [paramGetAPI getFloatValue:&brightness
                     fromParameter:1
                            atTime:renderTime];
        
        *pluginState = [NSData dataWithBytes:&brightness
                                      length:sizeof(brightness)];
        
        if (*pluginState != nil)
        {
            succeeded = YES;
        }
    }
    else
    {
        *error = [NSError errorWithDomain:FxPlugErrorDomain
                                     code:kFxError_ThirdPartyDeveloperStart + 20
                                 userInfo:@{
                                            NSLocalizedDescriptionKey :
                                                @"Unable to retrieve FxParameterRetrievalAPI_v6 in \
                                                [-TileableRemoteBrightness pluginStateAtTime:]" }];
    }
    
    return succeeded;
}
```

## See Also

### Plug-in fundamentals
- [Building an FxPlug plug-in from an Xcode template](./building-an-fxplug-plug-in-from-an-xcode-template.md)
  Create a plug-in in Xcode with the FxPlug template.
- [Building an FxPlug plug-in manually](./building-an-fxplug-plug-in-manually.md)
  Create your own plug-in in Xcode.
- [Editing property lists for FxPlug plug-ins](./editing-property-lists-for-fxplug-plug-ins.md)
  Modify the way hosts recognize and display your FxPlug plug-in.
- [Thread safety in plug-ins](./thread-safety-in-plug-ins.md)
  Learn about reentrancy for plug-ins and best practices to make them thread safe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/using-fxplug-apis)*