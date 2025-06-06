# init(name:)

**Framework**: Core Animation  
**Kind**: init

Returns the value function object identified by the name.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(name: CAValueFunctionName)
```

#### Return Value

A new `CAValueFunction` instance with the value function specified by the name.

#### Discussion

The possible values for `name` are specified in [`Rotate Value Functions`](rotate-value-functions.md), [`Scale Value Functions`](scale-value-functions.md), and [`Translate Functions`](translate-functions.md).

## Parameters

- `name`: The name of the value function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cavaluefunction/init(name:))*