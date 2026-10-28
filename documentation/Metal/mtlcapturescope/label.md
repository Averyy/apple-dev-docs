# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A string that helps you identify the capture scope.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

```objc
@property (atomic, copy, nullable) NSString * label;
```

## Discussion

Setting a capture scope’s label makes it easier to find in Xcode. See [Creating and using custom capture scopes](../../Xcode/creating-and-using-custom-capture-scopes.md) for more information.

## See Also

### Identifying the capture scope
- [var device: any MTLDevice](./device.md)
  The device object from which you created the capture scope.
- [var commandQueue: (any MTLCommandQueue)?](./commandqueue.md)
  The command queue that this capture scope uses to limit which commands are recorded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcapturescope/label)*