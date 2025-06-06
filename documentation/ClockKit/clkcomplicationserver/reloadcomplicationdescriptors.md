# reloadComplicationDescriptors()

**Framework**: ClockKit  
**Kind**: method

Reloads the complication descriptors from the complication data source.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
func reloadComplicationDescriptors()
```

## Mentions

- [Declaring complications for your app](declaring-complications-for-your-app.md)

#### Discussion

Call this method to reload the complication descriptors from your data source. ClockKit then calls your data source’s [`getComplicationDescriptors(handler:)`](clkcomplicationdatasource/getcomplicationdescriptors(handler:).md) method to update the list of available complications.

If your data source removes a complication that’s already present on a watch face, ClockKit continues to display the complication and to request new timeline entries for that complication. However, the user won’t be able to add the complication to new watch faces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/reloadcomplicationdescriptors())*