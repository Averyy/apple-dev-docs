# init(keyPath:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new parameter object using the specified key path and class information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+

## Declaration

```swift
@nonobjc
convenience init?<Root, Value>(keyPath: KeyPath<Root, Value>)
```

#### Return Value

An initialized parameter object.

## Parameters

- `keyPath`: Specifies a path to a value within a type.The intent or intent response class that acts as the root of the specified key path. For example, when specifying properties of a ride request intent, you would specify the [`INRequestRideIntent`](../inrequestrideintent.md) class. The path to a property of the specified class. For example, to specify the key path for the [`pickupLocation`](../inrequestrideintent/pickuplocation.md) property of a ride request, specify the string pickupLocation.

## See Also

### Creating a Parameter Object
- [convenience init(for: AnyClass, keyPath: String)](./init%28for,keypath%29.md)
  Creates a new parameter object using the specified key path and class information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inparameter/init(keypath:))*