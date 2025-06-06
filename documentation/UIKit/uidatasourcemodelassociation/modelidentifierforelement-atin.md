# modelIdentifierForElement(at:in:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the string that uniquely identifies the data at the specified location in the view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func modelIdentifierForElement(at idx: IndexPath, in view: UIView) -> String?
```

#### Return Value

A string that uniquely identifies the data object.

#### Discussion

Use the provided information to locate the requested data object. From that object, extract a string that can be used later to identify the same piece of data again. The string you return must not be based on transient information, such as the pointer to the current object in memory; it must instead be tied to the underlying data. In fact, if two different in-memory objects represent the same piece of data in your app, they must both return the same model identifier string.

## Parameters

- `idx`: The index path to the requested data object.
- `view`: The view that contains the data object.

## See Also

- [func indexPathForElement(withModelIdentifier: String, in: UIView) -> IndexPath?](uidatasourcemodelassociation/indexpathforelement(withmodelidentifier:in:).md)
  Returns the current index of the data object with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation/modelidentifierforelement(at:in:))*