# Hardened Heap

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the process opts in to type-aware memory allocations.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

#### Discussion

When you add this entitlement to your app or extension, the system uses the type-aware memory allocator for memory your app or extension requests. In addition to this entitlement, set the build settings `CLANG_ENABLE_C_TYPED_ALLOCATOR_SUPPORT` and `CLANG_ENABLE_CPLUSPLUS_TYPED_ALLOCATOR_SUPPORT` to `YES`, so the compiler rewrites memory allocations in your code to use the type-aware allocator.

Xcode adds this entitlement to your app or extension when you add the Enhanced Security capability. For more information, see [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/Xcode/enabling-enhanced-security-for-your-app).

## See Also

- [Hardened Process](entitlements/com.apple.security.hardened-process.md)
  A Boolean value that indicates whether the executable opts in to additional security checks.
- [Enhanced Security](entitlements/com.apple.security.hardened-process.enhanced-security-version.md)
  The entitlement required for an executable to opt in to enhanced security protections.
- [Additional Runtime Platform Restrictions](entitlements/com.apple.security.hardened-process.platform-restrictions.md)
  An integer value that indicates the level of additional runtime security protections your app or extension opts in to.
- [Enable Read-Only Platform Memory](entitlements/com.apple.security.hardened-process.dyld-ro.md)
  An entitlement that marks memory used for internal platform state as read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.hardened-heap)*