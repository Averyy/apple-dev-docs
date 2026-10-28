# init()

**Framework**: Scripting Bridge  
**Kind**: init  
**Role**: Initializer

Initializes and returns an instance of an `SBObject` subclass.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

## Return Value

An `SBObject` object or `nil` if the object could not be initialized.

## Discussion

Scripting Bridge does not actually create an object in the target application until you add the object returned from this method to an element array ([`SBElementArray`](../sbelementarray.md)).

## See Also

### Initializing a Scripting Bridge Object
- [init(data: Any)](./init%28data%29.md)
  Returns an instance of an `SBObject` subclass initialized with the given data.
- [init(properties: [AnyHashable : Any])](./init%28properties%29.md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties.
- [init(elementCode: DescType, properties: [String : Any]?, data: Any?)](./init%28elementcode,properties,data%29.md)
  Returns an instance of an `SBObject` subclass initialized with the specified properties and data and added to the designated element array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/init())*