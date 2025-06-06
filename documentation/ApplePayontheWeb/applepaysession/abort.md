# abort

**Framework**: Apple Pay on the Web  
**Kind**: method

Aborts the current Apple Pay session.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
undefined abort();
```

#### Discussion

Dismisses the payment sheet and ends the Apple Pay session without completing a transaction. Only the web page can call [`abort`](applepaysession/abort.md).

## See Also

- [oncancel](applepaysession/oncancel.md)
  An event handler that is automatically called when the payment UI is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/abort)*