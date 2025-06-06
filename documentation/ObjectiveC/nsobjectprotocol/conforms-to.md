# conforms(to:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the receiver conforms to a given protocol.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func conforms(to aProtocol: Protocol) -> Bool
```

#### Return Value

[`YES`](yes.md) if the receiver conforms to `aProtocol`, otherwise [`NO`](no.md).

#### Discussion

This method works identically to the [`conforms(to:)`](nsobject-swift.class/conforms(to:).md) class method declared in [`NSObject`](nsobject-swift.class.md). It’s provided as a convenience so that you don’t need to get the class object to find out whether an instance can respond to a given set of messages.

## Parameters

- `aProtocol`: A protocol object that represents a particular protocol.

## See Also

- [func isKind(of: AnyClass) -> Bool](nsobjectprotocol/iskind(of:).md)
  Returns a Boolean value that indicates whether the receiver is an instance of given class or an instance of any class that inherits from that class.
- [func isMember(of: AnyClass) -> Bool](nsobjectprotocol/ismember(of:).md)
  Returns a Boolean value that indicates whether the receiver is an instance of a given class.
- [func responds(to: Selector!) -> Bool](nsobjectprotocol/responds(to:).md)
  Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/conforms(to:))*