# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A string that identifies the rate map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get }
```

```objc
@property (readonly, nullable) NSString * label;
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. For more information, see [Naming resources and commands](../../Xcode/naming-resources-and-commands.md).

## See Also

### Identifying the rate map
- [var device: any MTLDevice](./device.md)
  The device object that created the rate map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemap/label)*