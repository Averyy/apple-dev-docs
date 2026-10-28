# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A string that identifies the texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get }
```

```objc
@property (readonly, nullable) NSString * label;
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../Xcode/naming-resources-and-commands.md).

## See Also

### Identifying the shared texture handle
- [var device: any MTLDevice](./device.md)
  The device object that created the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedtexturehandle/label)*