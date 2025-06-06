# init(value:andOwner:)

**Framework**: JavaScriptCore  
**Kind**: init

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

#### Return Value

A new managed value.

#### Discussion

Calling this method is equivalent to creating a managed value and then reporting it to the JavaScriptCore virtual machine using the [`addManagedReference(_:withOwner:)`](jsvirtualmachine/addmanagedreference(_:withowner:).md) method.

## Parameters

- `value`: A JavaScript value.
- `owner`: The Objective-C or Swift object responsible for

## See Also

- [init!(value: JSValue!)](jsmanagedvalue/init(value:).md)
  Initializes a managed value with the specified JavaScript value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue/init(value:andowner:))*