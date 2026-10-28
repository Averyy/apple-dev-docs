# managedValueWithValue:

**Framework**: JavaScriptCore  
**Kind**: method  
**Role**: Type Method

Creates a managed value with the specified JavaScript value.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (JSManagedValue *) managedValueWithValue:(JSValue *) value;
```

## Return Value

A new managed value.

## Discussion

To ensure that the underlying JavaScript value is retained as long as the managed value remains in use in the Objective-C or Swift runtime, report the managed value’s owner to the JavaScriptCore virtual machine using the [`addManagedReference(_:withOwner:)`](../jsvirtualmachine/addmanagedreference%28_,withowner%29.md) method.

## Parameters

- `value`: A JavaScript value.

## See Also

### Creating a Managed Value
- [init!(value: JSValue!)](./init%28value%29.md)
  Initializes a managed value with the specified JavaScript value.
- [init!(value: JSValue!, andOwner: Any!)](./init%28value,andowner%29.md)
  Creates a managed value and associates it with an owner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/managedvaluewithvalue:)*