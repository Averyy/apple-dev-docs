# showTipsForTesting(_:)

**Framework**: TipKit  
**Kind**: method  
**Role**: Type Method

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

## Overview

This function can also be called with the launch argument `-com.apple.TipKit.ShowTips FindTrailheadTip,SlopeProfileTip`.

Tip statuses automatically revert back to `available` after invalidation when displayed using this override to enable repeat testing of presentation and dismissal.

TipKit’s display override testing functions have the following precedence:

| Priority | Testing function |
| --- | --- |
| First | [`showTipsForTesting(_:)`](./showtipsfortesting%28_%29.md) |
| Second | [`hideTipsForTesting(_:)`](./hidetipsfortesting%28_%29.md) |
| Third | [`showAllTipsForTesting()`](./showalltipsfortesting%28%29.md) |
| Fourth | [`hideAllTipsForTesting()`](./hidealltipsfortesting%28%29.md) |

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

### Testing
- [static func showAllTipsForTesting()](./showalltipsfortesting%28%29.md)
  Show all tips regardless of their display rule eligibility or display frequency status for UI testing of tips.
- [static func hideAllTipsForTesting()](./hidealltipsfortesting%28%29.md)
  Hide all tips regardless of their display rule eligibility for UI testing without tips.
- [static func hideTipsForTesting([any Tip.Type])](./hidetipsfortesting%28_%29.md)
  Hide specified tips regardless of their display rule eligibility for UI testing without certain tips.
- [static func resetDatastore() throws](./resetdatastore%28%29.md)
  Resets the tips’ datastore to the initial state for re-testing tip display rules and eligibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/showtipsfortesting(_:))*