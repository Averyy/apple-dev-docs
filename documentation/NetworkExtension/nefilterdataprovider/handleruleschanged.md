# handleRulesChanged()

**Framework**: Network Extension  
**Kind**: method

Handle a rules changed event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func handleRulesChanged()
```

#### Discussion

The system calls this method when the Filter Control Provider calls the `notifyRulesChanged` method or returns a [`NEFilterControlVerdict`](nefiltercontrolverdict.md) with the [`updateRules()`](nefiltercontrolverdict/updaterules().md) property set to YES.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/handleruleschanged())*