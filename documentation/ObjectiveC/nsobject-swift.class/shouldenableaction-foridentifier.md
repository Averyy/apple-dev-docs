# shouldEnableAction(for:identifier:)

**Framework**: Objective-C Runtime  
**Kind**: method

Sent to the delegate to determine whether the action should be enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
func shouldEnableAction(for person: ABPerson!, identifier: String!) -> Bool
```

#### Return Value

[`YES`](yes.md) if the action is applicable; otherwise, [`NO`](no.md).

#### Discussion

If the property returned by [`actionProperty()`](nsobject-swift.class/actionproperty().md) is a multivalue property, `identifier` contains the unique identifier of the value selected.

## Parameters

- `person`: The person on which the action will be taken.
- `identifier`: The unique identifier of the selected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/shouldenableaction(for:identifier:))*