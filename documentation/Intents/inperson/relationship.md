# relationship

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The relationship between this person and the person using the device.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
var relationship: INPersonRelationship? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPersonRelationship relationship;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPersonRelationship relationship;
```

## Discussion

SiriKit sets the value of this property for you based on information provided by the user. For example, if the user says “send a message to my brother”, Siri sets this property to [`brother`](../inpersonrelationship/brother.md). However, if the user said “send a message to Shelly” and Shelly happened to be my spouse, Siri would not set this property.

## See Also

### Accessing relationship details
- [struct INPersonRelationship](../inpersonrelationship.md)
  Constants indicating the relationship between the person using the device and another person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/relationship)*