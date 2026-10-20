# MTRCommandWithRequiredResponse

**Framework**: Matter  
**Kind**: class  
**Role**: Class

An object representing a single command to be invoked and the response required for the invoke to be considered successful.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
class MTRCommandWithRequiredResponse
```

```objc
@interface MTRCommandWithRequiredResponse : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./mtrcommandwithrequiredresponse/init%28coder%29.md)
- [init(path: MTRCommandPath, commandFields: [String : Any]?, requiredResponse: [NSNumber : [String : Any]]?)](./mtrcommandwithrequiredresponse/init%28path,commandfields,requiredresponse%29.md)
### Instance Properties
- [var commandFields: [String : Any]?](./mtrcommandwithrequiredresponse/commandfields.md)
  The command fields to pass for the command invoke.  nil if this command does not have any fields.  If not nil, this should be a data-value dictionary of MTRStructureValueType.
- [var path: MTRCommandPath](./mtrcommandwithrequiredresponse/path.md)
  The path of the command being invoked.
- [var requiredResponse: [NSNumber : [String : Any]]?](./mtrcommandwithrequiredresponse/requiredresponse.md)
  The response that represents this command succeeding.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommandwithrequiredresponse)*