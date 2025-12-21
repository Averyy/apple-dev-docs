# performAction(for:identifier:)

**Framework**: Objective-C Runtime  
**Kind**: method

Sent to the delegate to perform the action.

**Availability**:
- macOS ?+

## Declaration

```swift
func performAction(for person: ABPerson!, identifier: String!)
```

#### Discussion

If the property returned by [`actionProperty()`](nsobject-swift.class/actionproperty().md) is a multivalue property, `identifier` contains the unique identifier of the value selected. The person being displayed in the Address Book application’s card view when the rollover menu is accesses is passed as `person`.

## Parameters

- `person`: The person on which the action will be taken.
- `identifier`: The unique identifier of the selected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/performaction(for:identifier:))*