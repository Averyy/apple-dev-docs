# responds(to:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.

**Availability**:
- iOS 1.0+
- iPadOS 1.0+
- Mac Catalyst 1.0+
- macOS 10.0+
- tvOS 1.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func responds(to aSelector: Selector!) -> Bool
```

#### Return Value

[`YES`](yes.md) if the receiver implements or inherits a method that can respond to `aSelector`, otherwise [`NO`](no.md).

#### Discussion

The application is responsible for determining whether a [`NO`](no.md) response should be considered an error.

You cannot test whether an object inherits a method from its superclass by sending [`responds(to:)`](nsobjectprotocol/responds(to:).md) to the object using the `super` keyword. This method will still be testing the object as a whole, not just the superclass’s implementation. Therefore, sending [`responds(to:)`](nsobjectprotocol/responds(to:).md) to `super` is equivalent to sending it to `self`. Instead, you must invoke the `NSObject` class method [`instancesRespond(to:)`](nsobject-swift.class/instancesrespond(to:).md) directly on the object’s superclass, as illustrated in the following code fragment.

```objc
if( [MySuperclass instancesRespondToSelector:@selector(aMethod)] ) {
    // invoke the inherited method
    [super aMethod];
}
```

You cannot simply use `[[self superclass] instancesRespondToSelector:@selector(aMethod)]` since this may cause the method to fail if it is invoked by a subclass.

Note that if the receiver is able to forward `aSelector` messages to another object, it will be able to respond to the message, albeit indirectly, even though this method returns [`NO`](no.md).

## Parameters

- `aSelector`: A selector that identifies a message.

## See Also

- [class func instancesRespond(to: Selector!) -> Bool](nsobject-swift.class/instancesrespond(to:).md)
  Returns a Boolean value that indicates whether instances of the receiver are capable of responding to a given selector.
- [func isKind(of: AnyClass) -> Bool](nsobjectprotocol/iskind(of:).md)
  Returns a Boolean value that indicates whether the receiver is an instance of given class or an instance of any class that inherits from that class.
- [func isMember(of: AnyClass) -> Bool](nsobjectprotocol/ismember(of:).md)
  Returns a Boolean value that indicates whether the receiver is an instance of a given class.
- [func conforms(to: Protocol) -> Bool](nsobjectprotocol/conforms(to:).md)
  Returns a Boolean value that indicates whether the receiver conforms to a given protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/responds(to:))*