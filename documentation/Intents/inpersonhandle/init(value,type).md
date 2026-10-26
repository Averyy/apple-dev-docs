# init(value:type:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes and returns a person handle with the specified data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
convenience init(value: String?, type: INPersonHandleType)
```

```objc
- (instancetype) initWithValue:(NSString *) value type:(INPersonHandleType) type;
```

#### Return Value

An initialized person handle object.

## Parameters

- `value`: The data to associate with the handle. Specify the data as a user-readable string.
- `type`: A constant indicating the type of information in the `value` parameter. For a list of possible values, see [`INPersonHandleType`](../inpersonhandletype.md).

## See Also

### Initializing a Person Handle
- [init(value: String?, type: INPersonHandleType, label: INPersonHandleLabel?)](./init%28value,type,label%29.md)
  Initializes and returns a person handle with the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpersonhandle/init(value:type:))*