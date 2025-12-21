# init(rawValue:)

**Framework**: Metal  
**Kind**: init

Creates a GPU family instance from a raw value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(rawValue: Int)
```

#### Discussion

You don’t need to call this initializer because it’s part of how Swift represents an enumeration from an Objective-C framework.

> 💡 **Tip**:  Use one of the [`MTLGPUFamily`](mtlgpufamily.md) cases, such as [`MTLGPUFamily.metal3`](mtlgpufamily/metal3.md), instead of this initializer.

## Parameters

- `rawValue`: An integer value that represents a GPU family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlgpufamily/init(rawvalue:))*