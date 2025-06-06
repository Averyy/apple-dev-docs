# showTipsForTesting(_:)

**Framework**: TipKit  
**Kind**: method

Show specified tips regardless of their display rule eligibility or display frequency status for UI testing of certain tips.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func showTipsForTesting(_ tips: [any Tip.Type])
```

#### Overview

This function can also be called with the launch argument `-com.apple.TipKit.ShowTips FindTrailheadTip,SlopeProfileTip`.

TipKit’s display override testing functions have the following precedence:

| Priority | Testing function |
| --- | --- |
| First | [`showTipsForTesting(_:)`](tips/showtipsfortesting(_:).md) |
| Second | [`hideTipsForTesting(_:)`](tips/hidetipsfortesting(_:).md) |
| Third | [`showAllTipsForTesting()`](tips/showalltipsfortesting().md) |
| Fourth | [`hideAllTipsForTesting()`](tips/hidealltipsfortesting().md) |

```swift
import SwiftUI
import TipKit

@main
struct LandmarkTips: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }

    init() {
        setupTips()
    }

    // Configure tips in the app.
    func setupTips() {
        do {
            #if DEBUG
            Tips.showTipsForTesting([FindTrailheadTip.self, SlopeProfileTip.self])
            #endif

            try Tips.configure()
        }
        catch {
            print("Error initializing TipKit \(error.localizedDescription)")
        }
    }
}
```

## Parameters

- `tips`: Array of tips to show regardless of their display rule eligibility.

## See Also

- [static func showAllTipsForTesting()](tips/showalltipsfortesting.md)
  Show all tips regardless of their display rule eligibility or display frequency status for UI testing of tips.
- [static func hideAllTipsForTesting()](tips/hidealltipsfortesting.md)
  Hide all tips regardless of their display rule eligibility for UI testing without tips.
- [static func hideTipsForTesting([any Tip.Type])](tips/hidetipsfortesting(_:).md)
  Hide specified tips regardless of their display rule eligibility for UI testing without certain tips.
- [static func resetDatastore() throws](tips/resetdatastore.md)
  Resets the tips’ datastore to the initial state for re-testing tip display rules and eligibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/showtipsfortesting(_:))*