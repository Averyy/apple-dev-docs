# isMember(of:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether the receiver is an instance of a given class.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func isMember(of aClass: AnyClass) -> Bool
```

```objc
- (BOOL) isMemberOfClass:(Class) aClass;
```

#### Return Value

[`YES`](../yes.md) if the receiver is an instance of `aClass`, otherwise [`NO`](../no.md).

#### Discussion

For example, in this code, [`isMember(of:)`](./ismember%28of%29.md) would return [`NO`](../no.md):

```objc
NSMutableData *myData = [NSMutableData dataWithCapacity:30];
id anArchiver = [[NSArchiver alloc] initForWritingWithMutableData:myData];
if ([anArchiver isMemberOfClass:[NSCoder class]])
    ...
```

Class objects may be compiler-created objects but they still support the concept of membership. Thus, you can use this method to verify that the receiver is a specific Class object.

## Parameters

- `aClass`: A class object representing the Objective-C class to be tested.

## See Also

### Testing Object Inheritance, Behavior, and Conformance
- [func isKind(of: AnyClass) -> Bool](./iskind%28of%29.md)
  Returns a Boolean value that indicates whether the receiver is an instance of given class or an instance of any class that inherits from that class.
- [func responds(to: Selector!) -> Bool](./responds%28to%29.md)
  Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.
- [func conforms(to: Protocol) -> Bool](./conforms%28to%29.md)
  Returns a Boolean value that indicates whether the receiver conforms to a given protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/ismember(of:))*