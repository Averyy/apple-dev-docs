---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/binarycrossentropy(logits:targets:weights:withlogits:reduction:)"
framework: "mlx-swift/MLXNN"
---

# binaryCrossEntropy(logits:targets:weights:withLogits:reduction:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Computes the binary cross entropy loss.

## Declaration

```swift
func binaryCrossEntropy(logits: MLXArray, targets: MLXArray, weights: MLXArray? = nil, withLogits: Bool = true, reduction: LossReduction = .mean) -> MLXArray
```

#### Return Value

Computed binary cross entropy loss

#### Discussion

By default, this function takes the pre-sigmoid logits, which results in a faster and more precise loss. For improved numerical stability when `withLogits` is true, the loss calculation clips the input probabilities (in log-space) to a minimum value of `-100`.

##### See Also

- [Loss Functions](./losses.md)

## Parameters

- `logits`: Unnormalized predicted logits
- `targets`: Binary target values in {0, 1}
- `weights`: Optional weights for each target
- `withLogits`: Whether the `logits` parameter is logits or probabilities
- `reduction`: Reduction type

## See Also

### Loss Functions
- [func cosineSimilarityLoss(x1: MLXArray, x2: MLXArray, axis: Int, eps: Float, reduction: LossReduction) -> MLXArray](./cosinesimilarityloss%28x1,x2,axis,eps,reduction%29.md)
  Computes the cosine similarity between the two inputs.
- [func crossEntropy(logits: MLXArray, targets: MLXArray, weights: MLXArray?, axis: Int, labelSmoothing: Float, reduction: LossReduction) -> MLXArray](./crossentropy%28logits,targets,weights,axis,labelsmoothing,reduction%29.md)
  Computes the cross entropy loss.
- [func hingeLoss(inputs: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./hingeloss%28inputs,targets,reduction%29.md)
  Computes the hinge loss between inputs and targets.
- [func huberLoss(inputs: MLXArray, targets: MLXArray, delta: Float, reduction: LossReduction) -> MLXArray](./huberloss%28inputs,targets,delta,reduction%29.md)
  Computes the Huber loss between inputs and targets.
- [func klDivLoss(inputs: MLXArray, targets: MLXArray, axis: Int, reduction: LossReduction) -> MLXArray](./kldivloss%28inputs,targets,axis,reduction%29.md)
  Computes the Kullback-Leibler divergence loss.
- [func l1Loss(predictions: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./l1loss%28predictions,targets,reduction%29.md)
  Computes the L1 loss
- [func logCoshLoss(inputs: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./logcoshloss%28inputs,targets,reduction%29.md)
  Computes the log cosh loss between inputs and targets.
- [func mseLoss(predictions: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./mseloss%28predictions,targets,reduction%29.md)
  Computes the mean squared error loss.
- [func nllLoss(inputs: MLXArray, targets: MLXArray, axis: Int, reduction: LossReduction) -> MLXArray](./nllloss%28inputs,targets,axis,reduction%29.md)
  Computes the negative log likelihood loss.
- [func smoothL1Loss(predictions: MLXArray, targets: MLXArray, beta: Float, reduction: LossReduction) -> MLXArray](./smoothl1loss%28predictions,targets,beta,reduction%29.md)
  Computes the smooth L1 loss.
- [func tripletLoss(anchors: MLXArray, positives: MLXArray, negatives: MLXArray, axis: Int, p: Int, margin: Float, eps: Float, reduction: LossReduction) -> MLXArray](./tripletloss%28anchors,positives,negatives,axis,p,margin,eps,reduction%29.md)
  Computes the triplet loss for a set of anchor, positive, and negative samples. Margin is represented with alpha in the math section.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/binarycrossentropy(logits:targets:weights:withlogits:reduction:))*