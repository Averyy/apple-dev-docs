# addPassesViewControllerDidFinish(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate after the add-passes view controller has finished.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func addPassesViewControllerDidFinish(_ controller: PKAddPassesViewController)
```

```objc
- (void) addPassesViewControllerDidFinish:(PKAddPassesViewController *) controller;
```

#### Discussion

When this optional method is implemented, the delegate is responsible for dismissing the view controller in `controller`.

## See Also

### Related Documentation
- [Wallet Developer Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/index.html#//apple_ref/doc/uid/TP40012195)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpassesviewcontrollerdelegate/addpassesviewcontrollerdidfinish(_:))*