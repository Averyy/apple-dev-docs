# showAllTipsForTesting()

**Framework**: TipKit  
**Kind**: method

Show all tips regardless of their display rule eligibility or display frequency status for UI testing of tips.

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
static func showAllTipsForTesting()
```

#### Overview

This function can also be called with the launch argument `-com.apple.TipKit.ShowAllTips 1`.

Tip statuses automatically revert back to `available` after invalidation when displayed using this override to enable repeat testing of presentation and dismissal.

TipKit’s display override testing functions have the following precedence:

| Priority | Testing function |
| --- | --- |
| first | [`showTipsForTesting(_:)`](tips/showtipsfortesting(_:).md) |
| second | [`hideTipsForTesting(_:)`](tips/hidetipsfortesting(_:).md) |
| third | [`showAllTipsForTesting()`](tips/showalltipsfortesting().md) |
| fourth | [`hideAllTipsForTesting()`](tips/hidealltipsfortesting().md) |

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
            Tips.showAllTipsForTesting()
            #endif

            try Tips.configure()
        }
        catch {
            print("Error initializing TipKit \(error.localizedDescription)")
        }
    }
}
```

## See Also

- [static func showTipsForTesting([any Tip.Type])](tips/showtipsfortesting(_:).md)
  Show specified tips regardless of their display rule eligibility or display frequency status for UI testing of certain tips.
- [static func hideAllTipsForTesting()](tips/hidealltipsfortesting.md)
  Hide all tips regardless of their display rule eligibility for UI testing without tips.
- [static func hideTipsForTesting([any Tip.Type])](tips/hidetipsfortesting(_:).md)
  Hide specified tips regardless of their display rule eligibility for UI testing without certain tips.
- [static func resetDatastore() throws](tips/resetdatastore.md)
  Resets the tips’ datastore to the initial state for re-testing tip display rules and eligibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/showalltipsfortesting())*