# init(elementCode:properties:data:)

**Framework**: Scripting Bridge  
**Kind**: init  
**Role**: Initializer

Returns an instance of an `SBObject` subclass initialized with the specified properties and data and added to the designated element array.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
init(elementCode code: DescType, properties: [String : Any]?, data: Any?)
```

```objc
- (instancetype) initWithElementCode:(DescType) code properties:(NSDictionary<NSString *,id> *) properties data:(id) data;
```

#### Return Value

An `SBObject` object or `nil` if the object could not be initialized.

#### Discussion

Unlike the other initializers of this class, this method not only initializes the `SBObject` object but adds it to a specified element array. This method is the designated initializer.

## Parameters

- `code`: A four-character code used to identify an element in the target application’s scripting interface. See [Apple Event Manager](../../applicationservices/apple_event_manager.md) for details.
- `properties`: A dictionary with [`NSNumber`](../../Foundation/nsnumber.md) keys specifying the four-character codes of properties (that is, attributes or to-one relationships) and the values for those properties. Pass `nil` if you are initializing the object by `data` only.
- `data`: An object containing data for the new `SBObject` object. The data varies according to the type of scripting object to be created. Pass `nil` if you initializing the object by `properties` only.

## See Also

### Initializing a Scripting Bridge Object
- [init()](./init%28%29.md)
  Initializes and returns an instance of an `SBObject` subclass.
- [init(data: Any)](./init%28data%29.md)
  Returns an instance of an `SBObject` subclass initialized with the given data.
- [init(properties: [AnyHashable : Any])](./init%28properties%29.md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/init(elementcode:properties:data:))*