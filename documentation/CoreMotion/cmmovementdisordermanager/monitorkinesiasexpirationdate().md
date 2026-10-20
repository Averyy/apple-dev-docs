# monitorKinesiasExpirationDate()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Returns the expiration date for the most recent monitoring period.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
func monitorKinesiasExpirationDate() -> Date?
```

```objc
- (NSDate *) monitorKinesiasExpirationDate;
```

#### Return Value

The current expiration date, or `nil` if you have not yet begun monitoring.

#### Discussion

This date is set when you call the [`monitorKinesias(forDuration:)`](./monitorkinesias%28forduration%29.md) method. You can extend the date by calling [`monitorKinesias(forDuration:)`](./monitorkinesias%28forduration%29.md) again; however, you can’t shorten the monitoring duration.

You can use the expiration date to determine whether you are currently monitoring the user.

```swift
guard let experiationDate = movementDisorderManager.monitorKinesiasExpirationDate() else {
    // You haven't started monitoring the user.
    return
}

if experiationDate > Date() {
    // Currently monitoring the user.
} else {
    // The monitoring period has ended.
}
```

## See Also

### Recording Movement Disorders
- [func monitorKinesias(forDuration: TimeInterval)](./monitorkinesias%28forduration%29.md)
  Calculate and store tremor and dyskinetic symptom results for the duration of the specified time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/monitorkinesiasexpirationdate())*