# maxTextureBindCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Determines the number of texture-binding slots for the argument table.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var maxTextureBindCount: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger maxTextureBindCount;
```

## Mentions

- [Understanding the Metal 4 core API](../understanding-the-metal-4-core-api.md)

## Discussion

The maximum value of this parameter is 128.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4argumenttabledescriptor/maxtexturebindcount)*