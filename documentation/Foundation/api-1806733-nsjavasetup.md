# NSJavaSetup

**Framework**: Foundation

Loads the Java virtual machine with specified parameters.

#### Overview

Part of the Java-to-Objective-C bridge. You normally shouldn’t use it yourself.

You can pass `nil` for the `plist` dictionary, in which case the Java virtual machine will not be loaded, so you should probably just use doc:object_runtime/java_support/1806737-nsjavasetupvirtualmachine instead. The `plist` dictionary may contain the following key-value pairs.

- `NSJavaRoot`—An NSString indicating the root of the location where the  application’s classes are.
- `NSJavaPath`—An NSArray of NSStrings, each string containing one component of a class path whose components will   be prepended by `NSJavaRoot` if they are not absolute locations.
- `NSJavaUserPath`—An NSString indicating another segment of the class path so that    the application developer can customize where the class loader should search for classes. When searching for classes, this path is searched after  the application’s class path so that one cannot replace the classes used by the application.
- `NSJavaLibraryPath`—An NSArray of NSStrings, each string containing one component of a path to search for dynamic shared libraries needed by Java wrappers.
- `NSJavaClasses`—An NSArray of NSStrings, each string containing the name of one class that the VM should load so that  their associated frameworks will be loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/1806733-nsjavasetup)*