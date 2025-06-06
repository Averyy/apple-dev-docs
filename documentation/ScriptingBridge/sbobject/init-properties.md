# init(properties:)

**Framework**: Scripting Bridge  
**Kind**: init

Returns an instance of an `SBObject` subclass initialized with the specified properties.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
init(properties: [AnyHashable : Any])
```

#### Return Value

An `SBObject` object or `nil` if the object could not be initialized.

#### Discussion

Scripting Bridge does not actually create an object in the target application until you add the object returned from this method to an element array ([`SBElementArray`](sbelementarray.md)).

## Parameters

- `properties`: A dictionary with keys specifying the names of properties   (that is, attributes or to-one relationships) and the values for those   properties.

## See Also

- [init()](sbobject/init.md)
  Initializes and returns an instance of an `SBObject` subclass.
- [init(data: Any)](sbobject/init(data:).md)
  Returns an instance of an `SBObject` subclass initialized with the given data.
- [init(elementCode: DescType, properties: [String : Any]?, data: Any?)](sbobject/init(elementcode:properties:data:).md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties and data and added to the designated element array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/init(properties:))*