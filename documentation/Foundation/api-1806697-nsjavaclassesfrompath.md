# NSJavaClassesFromPath

**Framework**: Foundation

Loads the Java classes located at the specified path.

#### Overview

Loads and returns the Java classes in the specified bundle. If the Java virtual machine is not loaded, load it first. A reference to the Java virtual machine is returned in the `vm` parameter. You can pass `nil` for the `vm` parameter if you do not want this information. Pass an array of names of classes to load in the `wanted` parameter. If you pass `nil` for the `wanted` parameter, all classes at the specified path will be loaded. Pass [`false`](https://developer.apple.com/documentation/Swift/false) for `usesyscl` if you want to use a new instance of the class loader to load the classes; otherwise, the system can reuse an existing instance of the class loader. If you pass [`false`](https://developer.apple.com/documentation/Swift/false) for `usesyscl`, the new class loader will be released when you are done with it; otherwise, the class loader will be cached for use next time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/1806697-nsjavaclassesfrompath)*