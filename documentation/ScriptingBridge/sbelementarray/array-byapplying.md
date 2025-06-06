# array(byApplying:)

**Framework**: Scripting Bridge  
**Kind**: method

Returns an array containing the results of sending the specified message to each object in the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func array(byApplying selector: Selector) -> [Any]
```

#### Return Value

A new array containing the results of sending the `selector` message to each object in the receiver, starting with the first object and continuing through the element array to the last object.

#### Discussion

The method identified by `selector` must not take any arguments and must return an Objective-C object. It should not have the side effect of modifying the receiving array. The order of the items in the result array corresponds to the order of the items in the original array.

## Parameters

- `selector`: A selector identifying the message to be sent to each object in   the array.

## See Also

- [func array(byApplying: Selector, with: Any) -> [Any]](sbelementarray/array(byapplying:with:).md)
  Returns an array containing the results of sending the specified message to each object in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/array(byapplying:))*