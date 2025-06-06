# instancesRespond(to:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a Boolean value that indicates whether instances of the receiver are capable of responding to a given selector.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func instancesRespond(to aSelector: Selector!) -> Bool
```

#### Return Value

[`YES`](yes.md) if instances of the receiver are capable of responding to `aSelector` messages, otherwise [`NO`](no.md).

#### Discussion

If `aSelector` messages are forwarded to other objects, instances of the class are able to receive those messages without error even though this method returns [`NO`](no.md).

To ask the class whether it, rather than its instances, can respond to a particular message, send to the class instead the  `NSObject` protocol instance method [`responds(to:)`](nsobjectprotocol/responds(to:).md).

## Parameters

- `aSelector`: A  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/instancesrespond(to:))*