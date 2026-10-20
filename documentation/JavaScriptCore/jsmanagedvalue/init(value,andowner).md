# init(value:andOwner:)

**Framework**: JavaScriptCore  
**Kind**: init  
**Role**: Initializer

Creates a managed value and associates it with an owner.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init!(value: JSValue!, andOwner owner: Any!)
```

```objc
+ (JSManagedValue *) managedValueWithValue:(JSValue *) value andOwner:(id) owner;
```

#### Return Value

A new managed value.

#### Discussion

Calling this method is equivalent to creating a managed value and then reporting it to the JavaScriptCore virtual machine using the [`addManagedReference(_:withOwner:)`](../jsvirtualmachine/addmanagedreference%28_,withowner%29.md) method.

## Parameters

- `value`: A JavaScript value.
- `owner`: The Objective-C or Swift object responsible for

## See Also

### Creating a Managed Value
- [init!(value: JSValue!)](./init%28value%29.md)
  Initializes a managed value with the specified JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/init(value:andowner:))*