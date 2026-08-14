# MPSFunction

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class MPSFunction
```

## Topics

### Initializers
- [init?(coder: NSCoder)](mpsfunction/init(coder:).md)
### Instance Properties
- [var device: any MTLDevice](mpsfunction/device.md)
- [var error: (any Error)?](mpsfunction/error.md)
  The error produced when attempting to build the function
- [var function: (any MTLFunction)?](mpsfunction/function.md)
  A MTLFunction that you can link into your shader
- [var name: String](mpsfunction/name.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](mpsfunction/copy(with:device:).md)
- [func functionPrototype() -> String](mpsfunction/functionprototype.md)
### Type Methods
- [class func supportsSecureCoding() -> Bool](mpsfunction/supportssecurecoding.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [MPSFColorConversion](mpsfcolorconversion.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsfunction)*