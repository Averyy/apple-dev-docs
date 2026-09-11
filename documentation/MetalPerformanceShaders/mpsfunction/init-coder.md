# init(coder:)

**Framework**: Metal Performance Shaders  
**Kind**: init

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init?(coder aDecoder: NSCoder)
```

#### Discussion

Called by NSCoder to decode MPSKernels

This standard method doesn’t allow for control over which device the object targets. By default this will be the Metal system default device. If you want another device, use the MPSKeyedUnarchiver or other  to decode the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsfunction/init(coder:))*