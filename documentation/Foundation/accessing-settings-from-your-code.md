# Accessing settings from your code

**Framework**: Foundation

Retrieve or change settings and monitor external changes to those values while your app runs.

#### Overview

Settings are data values that are external to your app, but which help you configure your app’s behavior and appearance. At runtime, you use settings to choose which code paths to run. For example, you might use settings to configure the units of measurement your app uses. You choose which settings your app supports and which ones people can configure.

To use settings in your code, fetch them from your [`UserDefaults`](userdefaults.md) object at the moment you need them. When defining settings, choose simple data types such as numbers, strings, dates, or URLs for values. Simple data types work better than complex types such as objects, because simple types are more portable from one version of your app to the next.

##### Register Your Apps Default Settings at Launch Time

Each [`UserDefaults`](userdefaults.md) object gives you a way to provide a complete set of initial settings before you need them. When your app launches, the only available settings are global settings and settings your app explicitly set the last time it ran. A newly installed app has no initial values, so you must set those values early in your app’s launch cycle. Setting a set of default values avoids the need to check for `nil` each time you fetch a setting.

To register a set of default settings, create a dictionary with all of your app’s setting keys and an appropriate set of initial values. Choose initial settings that put your app in a configuration that most people would want to use. At launch time, or early in your app’s life cycle, call the [`register(defaults:)`](userdefaults/register(defaults:).md) method and pass in the dictionary you created. This method places the provided defaults into the [`registrationDomain`](userdefaults/registrationdomain.md), making them the final choice when no other domain contains the same setting. For more information about domains, see [`UserDefaults`](userdefaults.md).

##### Configure a Swiftui View with Settings Data

If you use settings to configure your SwiftUI interface, wrap the variables you use to store those values with the [`AppStorage`](https://developer.apple.com/documentation/SwiftUI/AppStorage) property wrapper. Although you can fetch values from [`UserDefaults`](userdefaults.md) programmatically, the property wrapper automates the process of getting and setting the values.

The following example shows a view with a variable that retrieves its value from the app’s settings. The `"ShowLineNumbers"` value in the declaration is the setting key SwiftUI uses to get and set the value. The initial value in the declaration becomes the default value, which SwiftUI adds to the registration domain of the defaults database.

```swift
struct EditingPrefs: View {
    @AppStorage("ShowLineNumbers") var showLineNumbers = false

    var body: some View {
        Toggle("Show line numbers", isOn: $showLineNumbers) 
    }
}
```

SwiftUI retrieves settings from the standard defaults database unless you specify a different option. To use a different set of settings, add the [`defaultAppStorage(_:)`](https://developer.apple.com/documentation/SwiftUI/Scene/defaultAppStorage(_:)) modifier to your view. The parameter for this modifier is the [`UserDefaults`](userdefaults.md) object that you provide. Specify the object that contains the settings you want to use instead. For example, specify a defaults object that contains settings your app shares with an app extension.

##### Get and Set Stored Values Directly

Each [`UserDefaults`](userdefaults.md) object provides methods to get and set settings. Choose the method for the type of value you want and provide a key string with the name of the setting. The following code shows examples of how to use these methods to get and set assorted values:

```swift
let defaults = UserDefaults()
        
// Change settings.
let showLineNumbers = true
let title = "Hello, World!"
defaults.set(showLineNumbers, forKey: "ShowLineNumbers")
defaults.set(title, forKey: "TitleString")
defaults.set(true, forKey: "CacheDataAggressively")
        
// Retrieve settings.
let boolValue = defaults.bool(forKey: "ShowLineNumbers")
let stringValue = defaults.string(forKey: "TitleString")
```

When you assign a new value to a setting, your app’s local [`UserDefaults`](userdefaults.md) object updates its in-memory cache immediately, and subsequent requests for the same setting return the new value. If you share settings between processes, the system updates its own cache so that processes can access the new values. The system also writes the changes to disk asynchronously to ensure they persist between app launches.

##### Respond to External Changes to Settings

When a setting changes, you might need to update portions of your app to reflect the new value. Changes can occur from both inside and outside your app. You can monitor these changes in several ways:

- In a SwiftUI view, add the [`AppStorage`](https://developer.apple.com/documentation/SwiftUI/AppStorage) property wrapper to variables that store settings. SwiftUI updates the variable value in response to changes from both inside and outside your app.
- To detect changes that occur inside your app, register for a [`UserDefaults.DidChangeMessage`](userdefaults/didchangemessage.md) or [`didChangeNotification`](userdefaults/didchangenotification.md) with your `UserDefaults` object.
- To detect changes that occur outside your app, use key-value observing to monitor specific settings in your [`UserDefaults`](userdefaults.md) object. For example, use this approach to detect changes people make to your app-specific settings from the system Settings app. In macOS, external changes can also come from the `defaults` command-line tool.

The following example shows a type that uses key-value observing to monitor changes to a setting. After creating the object, a call to the `configureObserver` function registers the object as an observer of the `ShowLineNumbers` setting in the standard defaults database. When the value of that setting changes, the defaults system calls the object’s [`observeValue(forKeyPath:of:change:context:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/observeValue(forKeyPath:of:change:context:)) method to report the change. The system calls this method only when the actual value of the setting changes. If your code assigns a value to a setting, but the new value is the same as the old value, the defaults system doesn’t notify observers.

```swift
@objc class MyObserver: NSObject {
    let defaults = UserDefaults()
    
    func configureObserver() {
        defaults.addObserver(self, forKeyPath: "ShowLineNumbers", options: [.new, .old], context: nil)
    }
    
    override func observeValue(forKeyPath keyPath: String?, of object: Any?, 
                                                change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?) {
        print(“Setting changed: \(keyPath ?? "nil")")
    }
}
```

## See Also

- [class UserDefaults](userdefaults.md)
  An interface to the user’s defaults database, which stores system-wide and app-specific settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/accessing-settings-from-your-code)*