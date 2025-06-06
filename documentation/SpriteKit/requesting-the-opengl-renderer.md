# Requesting the OpenGL Renderer

**Framework**: Spritekit

Switch to the legacy renderer temporarily for debugging purposes.

#### Overview

By default, SpriteKit renders with Metal in iOS 9 and OS X 10.11, but you can request the OpenGL renderer by adding the  key to your app’s  and giving it a boolean value of .

> ❗ **Important**:  This key applies to SceneKit content, too. So if your app uses SceneKit within SpriteKit, or displays SceneKit content on its own, that content will also be affected by this key.

##### Displaying the Currently Active Renderer

SpriteKit migrated from being implemented in OpenGL to Metal in iOS 9, but there are still situations where the OpenGL renderer might be active, for example:

- Apps that have specifically requested the OpenGL renderer. See (requesting the OpenGL renderer)
- Apps running on an iOS device that does not support Metal

In these situations, it might be handy to see which renderer is active at run time. The following code listing shows the code to do that:

```swift
// Get the standard user defaults
let defaults = UserDefaults.standard

// Create a new string-keyed dictionary of any value type
var dict = [String:Any]()

// Set the SKContextType debug draw statistics to true
dict["debugDrawStats_SKContextType"] = true

// Supply the dictionary with the SpriteKit defaults key
defaults.set( dict, forKey: "SKDefaults" )        
```

> **Note**:  You should add this code within your app’s initialization code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SpriteKit/requesting-the-opengl-renderer)*