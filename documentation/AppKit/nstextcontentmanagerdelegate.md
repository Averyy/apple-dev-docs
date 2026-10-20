# NSTextContentManagerDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

The optional methods that delegates of content manager objects implement for customizing or validating text elements.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol NSTextContentManagerDelegate : NSObjectProtocol
```

```objc
@protocol NSTextContentManagerDelegate <NSObject>
```

## Topics

### Finding a text element at a specific location
- [func textContentManager(NSTextContentManager, textElementAt: any NSTextLocation) -> NSTextElement?](./nstextcontentmanagerdelegate/textcontentmanager%28_,textelementat%29.md)
  The method the framework calls to return the text element at a specific location.
### Validating a text element
- [func textContentManager(NSTextContentManager, shouldEnumerate: NSTextElement, options: NSTextContentManager.EnumerationOptions) -> Bool](./nstextcontentmanagerdelegate/textcontentmanager%28_,shouldenumerate,options%29.md)
  Returns a Boolean value that indicates whether the framework should skip this text element in the enumeration.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [NSTextContentStorageDelegate](./nstextcontentstoragedelegate.md)

## See Also

### Customizing and validating text elements
- [var delegate: (any NSTextContentManagerDelegate)?](./nstextcontentmanager/delegate.md)
  The delegate for the content manager object.
- [NSTextContentManager.EnumerationOptions](./nstextcontentmanager/enumerationoptions.md)
  Values that control the order in which the framework enumerates text elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentmanagerdelegate)*