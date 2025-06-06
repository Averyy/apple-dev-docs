# Migrating Your Objective-C Code to Swift

**Framework**: Swift

Learn the recommended steps to migrate your code.

#### Overview

You can improve the architecture, logic, and performance of one of your Objective-C apps by replacing pieces of it in Swift.  Interoperability makes it possible to integrate features migrated to Swift into Objective-C code with no hassle. You don’t need to rewrite your entire app in Swift at once.

##### Clean Up Your Code

Make sure that your Objective-C code and Swift code have optimal compatibility by tidying up and modernizing your existing Objective-C codebase. For example, if there are parts of your codebase to which you haven’t added nullability annotations, now’s the time to add them. Make sure your code follows modern coding practices so that it interacts more effectively with Swift.

##### Migrate Your Code

The most effective approach for migrating code to Swift is on a per-file basis—that is, one class at a time. Because you can’t subclass Swift classes in Objective-C, it’s best to choose a class in your app that doesn’t have any subclasses. You’ll replace the `.m` and `.h` files for that class with a single `.swift` file. Everything from your implementation and interface goes directly into this single Swift file. You won’t create a header file; Xcode generates a header automatically in case you need to reference it.

1. Create a Swift class for your corresponding Objective-C .m and .h files by choosing File > New > File > (iOS, watchOS, tvOS, or macOS) > Source > Swift File. You can use the same or a different name than your Objective-C class. Class prefixes are optional in Swift.
2. Import relevant system frameworks.
3. Fill out an Objective-C bridging header if you need to access Objective-C code from the same app target in your Swift file.
4. To make your Swift class accessible and usable back in Objective-C, make it a descendant of an Objective-C class. To specify a particular name for the class to use in Objective-C, mark it with `@objc(``)`, where name is the name that your Objective-C code uses to reference the Swift class.

###### As You Work

1. You can set up your Swift class to integrate Objective-C behavior by subclassing Objective-C classes, adopting Objective-C protocols, and more.
2. As you work with Objective-C APIs, you’ll need to know how Swift translates certain Objective-C language features. For more information, see [`Objective-C and C Code Customization`](objective-c-and-c-code-customization.md).
3. Use the `@objc(``)` attribute to provide Objective-C names for properties and methods when necessary.
4. Denote instance (`-`) and class (`+`) methods with `func` and `class func`, respectively.
5. Declare simple macros as global constants, and translate complex macros into functions.

###### After You Finish

1. Update import statements in your Objective-C code (to `#import "ProductModuleName-Swift.h"`) to refer to your new Swift code.
2. Remove the original Objective-C `.m` file from the target by deselecting the target membership checkbox. Don’t delete the `.m` and `.h` files immediately; use them to troubleshoot.
3. Update your code to use the Swift class name instead of the Objective-C name if you gave the Swift class a different name.

##### Troubleshooting Tips and Reminders

Migration experiences differ depending on your existing codebase, but here are some general steps and tools to help you troubleshoot the process:

- Remember that you can’t subclass a Swift class in Objective-C. Therefore, the class you migrate can’t have any Objective-C subclasses.
- Once you migrate a class to Swift, you must remove the corresponding `.m` file from the target before building to avoid a duplicate symbol error.
- To make a Swift class available in Objective-C, make it a descendant of an Objective-C class.
- Command-click a Swift class name to see its generated header.
- Option-click a symbol to see implicit information about it, like its type, attributes, and documentation comments.

## See Also

- [Objective-C and C Code Customization](objective-c-and-c-code-customization.md)
  Apply macros to your Objective-C APIs to customize how they’re imported into Swift.
- [Cocoa Design Patterns](cocoa-design-patterns.md)
  Adopt and interoperate with Cocoa design patterns in your Swift apps.
- [Handling Dynamically Typed Methods and Objects in Swift](handling-dynamically-typed-methods-and-objects-in-swift.md)
  Cast instances of the Objective-C `id` type to a specific Swift type.
- [Using Objective-C Runtime Features in Swift](using-objective-c-runtime-features-in-swift.md)
  Use selectors and key paths to interact with dynamic Objective-C APIs.
- [Imported C and Objective-C APIs](imported-c-and-objective-c-apis.md)
  Use native Swift syntax to interoperate with types and functions in C and Objective-C.
- [Calling Objective-C APIs Asynchronously](calling-objective-c-apis-asynchronously.md)
  Learn how functions and methods that take a completion handler are converted to Swift asynchronous functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/migrating-your-objective-c-code-to-swift)*