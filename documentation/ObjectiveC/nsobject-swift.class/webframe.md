# webFrame

**Framework**: Objective-C Runtime  
**Kind**: property  
**Role**: Instance Property

Returns the `WebFrame` that contains the plug-in.

**Availability**:
- macOS

## Declaration

```swift
var webFrame: WebFrame! { get }
```

```objc
@property (nonatomic, strong, readonly) WebFrame * webFrame;
```

## Return Value

The WebFrame that contains the plug-in.

## Discussion

Only implemented by containers that are based on the WebKit’s plug-in architecture.

## See Also

### Obtaining information about the container
- [var webPlugInContainerSelectionColor: NSColor!](./webplugincontainerselectioncolor.md)
  Returns the plug-in selection color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webframe)*