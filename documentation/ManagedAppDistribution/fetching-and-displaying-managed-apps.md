# Fetching and displaying managed apps

**Framework**: ManagedAppDistribution

Provide a consistent app presentation when displaying managed apps.

#### Overview

Your app can take advantage of Managed App Distribution features to display download status and launch apps. Obtain a list of [`ManagedApp`](managedapp.md) objects, then display that list of apps in a custom view.

##### Fetching

This code snippet defines a model that obtains a list of apps from a [`ManagedAppLibrary`](managedapplibrary.md).

```swift
import ManagedAppDistribution
import Observation

// Define a model that obtains a list of managed apps.
@Observable final class ViewModel {
    var content: [Content] = []
    enum Content {
        case managedApp(ManagedApp), developerContent(title: String, action: () -> Void)
    }

    func getApps() async {
        do {
            for try await result in ManagedAppLibrary.currentDistributor.availableApps {
                content = try result.get().map(Content.managedApp)
            }
        } catch {
            // Handle errors here.
        }
    }
}
```

##### Displaying

After you fetch the list of apps from the model, display them in a compact content style within your custom view.

![An image of the bottom of an iPhone showing an app with a banner that contains a title, subtitle, and an install button.](https://docs-assets.developer.apple.com/published/580c12870254422a479ee299ff61ae92/fetching-displaying-managed-apps%402x.png)

This code snippet demonstrates how to display the list of apps.

```swift
import ManagedAppDistribution
import SwiftUI

struct AppList: View {
    private var viewModel = ViewModel()
    var body: some View {
        List(viewModel.content) { content in
            switch content {
            case let .managedApp(managedApp): 
                ManagedAppView(app: managedApp)
            case let .developerContent(title, action): 
                ManagedContentView(primaryText: title, offerState: .custom("Request"), offerAction: action) {
                    Image(name: "custom")
                }
            }
        }
        .managedContentStyle(.compact)
        .task { await viewModel.getApps() }
    }
}
```

## See Also

- [struct ManagedApp](managedapp.md)
  A representation of a managed app.
- [class ManagedAppLibrary](managedapplibrary.md)
  A representation of a library of managed apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/fetching-and-displaying-managed-apps)*