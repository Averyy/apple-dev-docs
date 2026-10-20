# MPSFunction

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class MPSFunction
```

```objc
@interface MPSFunction : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./mpsfunction/init%28coder%29.md)
### Instance Properties
- [var device: any MTLDevice](./mpsfunction/device.md)
- [var error: (any Error)?](./mpsfunction/error.md)
  The error produced when attempting to build the function
- [var function: (any MTLFunction)?](./mpsfunction/function.md)
  A MTLFunction that you can link into your shader
- [var name: String](./mpsfunction/name.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpsfunction/copy%28with,device%29.md)
- [func functionPrototype() -> String](./mpsfunction/functionprototype%28%29.md)
### Type Methods
- [class func supportsSecureCoding() -> Bool](./mpsfunction/supportssecurecoding%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MPSFColorConversion](./mpsfcolorconversion.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsfunction)*