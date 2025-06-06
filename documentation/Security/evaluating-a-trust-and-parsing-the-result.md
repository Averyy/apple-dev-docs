# Evaluating a Trust and Parsing the Result

**Framework**: Security

Learn what to expect when evaluating a trust object.

#### Overview

Using the trust object that you obtained in [`Creating a Trust Object`](creating-a-trust-object.md), you evaluate it with the [`SecTrustEvaluateAsyncWithError(_:_:_:)`](sectrustevaluateasyncwitherror(_:_:_:).md) method:

If the trust object already has a result, the evaluation might invoke the callback synchronously, before the method returns. In other cases, like when the evaluation needs to fetch intermediate certificates or perform revocation checking, it might instead return immediately, perform the evaluation asynchronously, and call the closure later with a result. Either way, you must call the evaluation method on the same thread that you specify for the closure.

When the evaluation finishes and the method invokes the callback, examine the `result` parameter. If the trust result is `true`, the evaluation succeeded. At this point, you can get the public key from the leaf certificate with [`SecTrustCopyPublicKey(_:)`](sectrustcopypublickey(_:).md), as explained in [`Getting an Existing Key`](getting-an-existing-key.md), and begin to use it. If the result is `false`, you might be able to recover from the failure, as described in [`Discovering Why a Trust Evaluation Failed`](discovering-why-a-trust-evaluation-failed.md). If you can’t recover—for example, because the certificate is revoked—handle the failure gracefully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/evaluating-a-trust-and-parsing-the-result)*