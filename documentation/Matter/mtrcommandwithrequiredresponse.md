# MTRCommandWithRequiredResponse

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init(path: MTRCommandPath, commandFields: [String : Any]?, requiredResponse: [NSNumber : [String : Any]]?)](mtrcommandwithrequiredresponse/init(path:commandfields:requiredresponse:).md)
### Instance Properties
- [var commandFields: [String : Any]?](mtrcommandwithrequiredresponse/commandfields.md)
  The command fields to pass for the command invoke.  nil if this command does not have any fields.  If not nil, this should be a data-value dictionary of MTRStructureValueType.
- [var path: MTRCommandPath](mtrcommandwithrequiredresponse/path.md)
  The path of the command being invoked.
- [var requiredResponse: [NSNumber : [String : Any]]?](mtrcommandwithrequiredresponse/requiredresponse.md)
  The response that represents this command succeeding.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcommandwithrequiredresponse)*