# Evaluating a Boolean value

**Framework**: App Store Connect API

Return given values for true and false results of a conditional.

#### Overview

Use the `if()` function in the expression of a matchmaking rule to return values depending on a Boolean conditional. For example, `if (true, `0.0`, `1.0`)` returns `0.0`, and `if (false, `0.0`, `1.0`)` returns `1.0`.

##### Declaration

```swift
any if(boolean $condition, any $ifTrue, any $ifFalse)
```

##### Parameters

##### Return Value

Returns `ifTrue` if `condition` is `true`; otherwise, `ifFalse`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/evaluating-a-boolean-value)*