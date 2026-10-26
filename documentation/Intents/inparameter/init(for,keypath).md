# init(for:keyPath:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new parameter object using the specified key path and class information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
convenience init(for aClass: AnyClass, keyPath: String)
```

```objc
+ (instancetype) parameterForClass:(Class) aClass keyPath:(NSString *) keyPath;
```

#### Return Value

An initialized parameter object.

#### Discussion

If any properties in the key path contain an array or ordered set, use the [`setIndex(_:forSubKeyPath:)`](./setindex%28_,forsubkeypath%29.md) method to specify which object in those properties to use.

## Parameters

- `aClass`: The intent or intent response class that contains the specified key path. For example, when specifying properties of a ride request intent, you would specify the [`INRequestRideIntent`](../inrequestrideintent.md) class.
- `keyPath`: The path to a property of the specified class. For example, to specify the key path for the [`pickupLocation`](../inrequestrideintent/pickuplocation.md) property of a ride request, specify the string `pickupLocation`.

## See Also

### Creating a Parameter Object
- [convenience init?<Root, Value>(keyPath: KeyPath<Root, Value>)](./init%28keypath%29.md)
  Creates a new parameter object using the specified key path and class information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inparameter/init(for:keypath:))*