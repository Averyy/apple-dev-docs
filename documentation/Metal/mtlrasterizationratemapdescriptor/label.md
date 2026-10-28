# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A string used to identify the rate map you create with the descriptor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * label;
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../Xcode/naming-resources-and-commands.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/label)*