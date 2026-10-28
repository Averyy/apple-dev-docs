# resetDatastore()

**Framework**: TipKit  
**Kind**: method  
**Role**: Type Method

Resets the tips’ datastore to the initial state for re-testing tip display rules and eligibility.

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
static func resetDatastore() throws
```

## Overview

Must be called before [`configure(_:)`](./configure%28_%29.md).

This function can also be called with the launch argument `-com.apple.TipKit.ResetDatastore 1`.

> ❗ **Important**: This function removes the existing tip, event, and parameter records from your app’s TipKit datastore and will cause previously dismissed tips to become re-eligible for display. It is primarily designed for testing your app’s first launch experience.

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
            try Tips.resetDatastore()
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

### Testing
- [static func showAllTipsForTesting()](./showalltipsfortesting%28%29.md)
  Show all tips regardless of their display rule eligibility or display frequency status for UI testing of tips.
- [static func showTipsForTesting([any Tip.Type])](./showtipsfortesting%28_%29.md)
  Show specified tips regardless of their display rule eligibility or display frequency status for UI testing of certain tips.
- [static func hideAllTipsForTesting()](./hidealltipsfortesting%28%29.md)
  Hide all tips regardless of their display rule eligibility for UI testing without tips.
- [static func hideTipsForTesting([any Tip.Type])](./hidetipsfortesting%28_%29.md)
  Hide specified tips regardless of their display rule eligibility for UI testing without certain tips.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/resetdatastore())*