# Randomization Services

**Framework**: Security  
**Role**: API Collection

Generate cryptographically secure random numbers.

#### Overview

Many security operations rely on randomization to avoid reproducibility. This is true for many complex cryptographic operations, such as key generation, but is also true for something as simple as generating a password string that can’t be easily guessed. If the string’s characters are truly random (and kept hidden), an attacker has no choice but to try every possible combination one at a time in a brute force attack. For sufficiently long strings, this becomes unfeasible.

But the strength of such a password depends on the quality of the randomization. True randomization is not possible in a deterministic system, such as one where software instructions from a bounded set are executed according to well-defined rules. But even “good” randomization (in a statistical sense) is difficult to produce under these conditions. If an attacker can infer patterns in insufficiently randomized data, your system becomes compromised. Use randomization services to generate a cryptographically secure set of random numbers.

![Diagram showing random number generation.](https://developer.apple.com/tutorials/images/com.apple.security/media-2903623@2x.png)

## Topics

### Random Numbers
- [func SecRandomCopyBytes(SecRandomRef?, Int, UnsafeMutableRawPointer) -> Int32](./secrandomcopybytes%28_,_,_%29.md)
  Generates an array of cryptographically secure random bytes.
- [typealias SecRandomRef](./secrandomref.md)
  An abstract Core Foundation-type object containing information about a random number generator.
- [let kSecRandomDefault: SecRandomRef](./ksecrandomdefault.md)
  An alias for the default random number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/randomization-services)*